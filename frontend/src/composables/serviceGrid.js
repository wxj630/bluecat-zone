export default function articleGrid() {

    const gridStyle = (service) => {
        return _gridStyle(service)
    };

    return {
        gridStyle,
    }
}


function _gridStyle(service) {
    if (service.avatar) {
        return {
            display: 'grid',
            gridTemplateColumns: '1fr 4fr'
        }
    }
}